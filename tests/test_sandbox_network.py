from http import HTTPStatus
from unittest import TestCase
from unittest.mock import patch

from sandbox0 import Client
from sandbox0.apispec.models.credential_binding import CredentialBinding
from sandbox0.apispec.models.credential_projection_type import CredentialProjectionType
from sandbox0.apispec.models.egress_auth_failure_policy import EgressAuthFailurePolicy
from sandbox0.apispec.models.egress_auth_protocol import EgressAuthProtocol
from sandbox0.apispec.models.egress_credential_rule import EgressCredentialRule
from sandbox0.apispec.models.egress_proxy_policy import EgressProxyPolicy
from sandbox0.apispec.models.egress_proxy_type import EgressProxyType
from sandbox0.apispec.models.egress_tls_mode import EgressTLSMode
from sandbox0.apispec.models.http_match import HTTPMatch
from sandbox0.apispec.models.mcp_protocol_rule import MCPProtocolRule
from sandbox0.apispec.models.mcp_tool_policy import MCPToolPolicy
from sandbox0.apispec.models.network_egress_policy import NetworkEgressPolicy
from sandbox0.apispec.models.placeholder_replacement import PlaceholderReplacement
from sandbox0.apispec.models.placeholder_substitution_location import (
    PlaceholderSubstitutionLocation,
)
from sandbox0.apispec.models.placeholder_substitution_projection import (
    PlaceholderSubstitutionProjection,
)
from sandbox0.apispec.models.port_spec import PortSpec
from sandbox0.apispec.models.projection_spec import ProjectionSpec
from sandbox0.apispec.models.protocol_rule import ProtocolRule
from sandbox0.apispec.models.protocol_rule_protocol import ProtocolRuleProtocol
from sandbox0.apispec.models.sandbox_network_policy import SandboxNetworkPolicy
from sandbox0.apispec.models.sandbox_network_policy_mode import SandboxNetworkPolicyMode
from sandbox0.apispec.models.success_sandbox_network_policy_response import (
    SuccessSandboxNetworkPolicyResponse,
)
from sandbox0.apispec.models.traffic_rule import TrafficRule
from sandbox0.apispec.models.traffic_rule_action import TrafficRuleAction
from sandbox0.apispec.models.traffic_rule_app_protocol import TrafficRuleAppProtocol
from sandbox0.apispec.models.username_password_projection import (
    UsernamePasswordProjection,
)
from sandbox0.apispec.types import Response
from sandbox0.sandbox import Sandbox


class TestSandboxNetwork(TestCase):
    def test_update_network_policy_with_socks5_proxy_credential_binding(self) -> None:
        client = Client(token="test-token", base_url="https://example.com")
        self.addCleanup(client.close)

        sandbox = Sandbox(id="sb_123", client=client)
        captured = {}
        policy = SandboxNetworkPolicy(
            mode=SandboxNetworkPolicyMode.BLOCK_ALL,
            egress=NetworkEgressPolicy(
                traffic_rules=[
                    TrafficRule(
                        name="internal-api",
                        action=TrafficRuleAction.ALLOW,
                        domains=["api.internal.example.com"],
                        app_protocols=[TrafficRuleAppProtocol.TLS],
                    )
                ],
                protocol_rules=[
                    ProtocolRule(
                        name="internal-mcp",
                        protocol=ProtocolRuleProtocol.MCP,
                        domains=["api.internal.example.com"],
                        ports=[PortSpec(port=443, protocol="tcp")],
                        tls_mode=EgressTLSMode.TERMINATE_REORIGINATE,
                        http_match=HTTPMatch(methods=["POST"], paths=["/mcp"]),
                        mcp=MCPProtocolRule(
                            tools=MCPToolPolicy(
                                allowed=["read_file"],
                                denied=["run_command"],
                            ),
                        ),
                    )
                ],
                proxy=EgressProxyPolicy(
                    type_=EgressProxyType.SOCKS5,
                    address="proxy.example.com:1080",
                    credential_ref="corp-proxy",
                ),
            ),
            credential_bindings=[
                CredentialBinding(
                    ref="corp-proxy",
                    source_ref="corp-proxy-source",
                    projection=ProjectionSpec(
                        type_=CredentialProjectionType.USERNAME_PASSWORD,
                        username_password=UsernamePasswordProjection(),
                    ),
                )
            ],
        )

        def fake_sync_detailed(*, id, client, body):
            captured["id"] = id
            captured["body"] = body
            return Response(
                status_code=HTTPStatus.OK,
                content=b"{}",
                headers={},
                parsed=SuccessSandboxNetworkPolicyResponse(success=True, data=body),
            )

        with patch(
            "sandbox0.sandbox_network.put_api_v1_sandboxes_id_network.sync_detailed",
            side_effect=fake_sync_detailed,
        ):
            updated = sandbox.update_network_policy(policy)

        self.assertIs(updated, policy)
        self.assertEqual(captured["id"], "sb_123")
        self.assertIs(captured["body"], policy)
        self.assertEqual(policy.egress.protocol_rules[0].protocol, ProtocolRuleProtocol.MCP)
        self.assertEqual(policy.egress.protocol_rules[0].mcp.tools.allowed, ["read_file"])
        self.assertEqual(policy.egress.protocol_rules[0].mcp.tools.denied, ["run_command"])
        self.assertEqual(policy.egress.proxy.type_, EgressProxyType.SOCKS5)
        self.assertEqual(policy.egress.proxy.address, "proxy.example.com:1080")
        self.assertEqual(
            policy.credential_bindings[0].projection.type_,
            CredentialProjectionType.USERNAME_PASSWORD,
        )

    def test_update_network_policy_with_placeholder_substitution_binding(self) -> None:
        client = Client(token="test-token", base_url="https://example.com")
        self.addCleanup(client.close)

        sandbox = Sandbox(id="sb_123", client=client)
        captured = {}
        policy = SandboxNetworkPolicy(
            mode=SandboxNetworkPolicyMode.BLOCK_ALL,
            egress=NetworkEgressPolicy(
                traffic_rules=[
                    TrafficRule(
                        name="allow-example-api",
                        action=TrafficRuleAction.ALLOW,
                        cidrs=["203.0.113.10/32"],
                        ports=[PortSpec(port=8080, protocol="tcp")],
                    )
                ],
                credential_rules=[
                    EgressCredentialRule(
                        name="api-token",
                        credential_ref="api-token",
                        protocol=EgressAuthProtocol.HTTP,
                        ports=[PortSpec(port=8080, protocol="tcp")],
                        failure_policy=EgressAuthFailurePolicy.FAIL_CLOSED,
                    )
                ],
            ),
            credential_bindings=[
                CredentialBinding(
                    ref="api-token",
                    source_ref="api-token-source",
                    projection=ProjectionSpec(
                        type_=CredentialProjectionType.PLACEHOLDER_SUBSTITUTION,
                        placeholder_substitution=PlaceholderSubstitutionProjection(
                            replacements=[
                                PlaceholderReplacement(
                                    placeholder="s0env_api_token",
                                    value_template="{{ .token }}",
                                    locations=[
                                        PlaceholderSubstitutionLocation.QUERY,
                                        PlaceholderSubstitutionLocation.HEADER,
                                        PlaceholderSubstitutionLocation.BODY,
                                    ],
                                )
                            ]
                        ),
                    ),
                )
            ],
        )

        def fake_sync_detailed(*, id, client, body):
            captured["id"] = id
            captured["body"] = body
            return Response(
                status_code=HTTPStatus.OK,
                content=b"{}",
                headers={},
                parsed=SuccessSandboxNetworkPolicyResponse(success=True, data=body),
            )

        with patch(
            "sandbox0.sandbox_network.put_api_v1_sandboxes_id_network.sync_detailed",
            side_effect=fake_sync_detailed,
        ):
            updated = sandbox.update_network_policy(policy)

        self.assertIs(updated, policy)
        self.assertEqual(captured["id"], "sb_123")
        self.assertIs(captured["body"], policy)
        self.assertEqual(
            policy.to_dict()["credentialBindings"][0]["projection"],
            {
                "type": "placeholder_substitution",
                "placeholderSubstitution": {
                    "replacements": [
                        {
                            "placeholder": "s0env_api_token",
                            "valueTemplate": "{{ .token }}",
                            "locations": ["query", "header", "body"],
                        }
                    ]
                },
            },
        )
