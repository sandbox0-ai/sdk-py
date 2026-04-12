import time
import unittest

from sandbox0.apispec.api.templates.delete_api_v1_templates_id import sync_detailed as delete_template
from sandbox0.apispec.api.templates.get_api_v1_templates import sync_detailed as list_templates
from sandbox0.apispec.api.templates.get_api_v1_templates_id import sync_detailed as get_template
from sandbox0.apispec.api.templates.post_api_v1_templates import sync_detailed as create_template
from sandbox0.apispec.api.templates.put_api_v1_templates_id import sync_detailed as update_template
from sandbox0.apispec.models.success_template_list_response import SuccessTemplateListResponse
from sandbox0.apispec.models.success_message_response import SuccessMessageResponse
from sandbox0.apispec.models.success_template_response import SuccessTemplateResponse
from sandbox0.apispec.models.template_create_request import TemplateCreateRequest
from sandbox0.apispec.models.template_update_request import TemplateUpdateRequest
from sandbox0.apispec.models.warm_process_spec import WarmProcessSpec
from sandbox0.apispec.models.warm_process_spec_type import WarmProcessSpecType
from sandbox0.response import ensure_data, ensure_model

from tests.e2e.helpers import close_client, new_client, require_config


class TestTemplates(unittest.TestCase):
    def test_template_crud(self) -> None:
        cfg = require_config(self)
        client = new_client(cfg)
        self.addCleanup(close_client, client)

        list_resp = list_templates(client=client.api)
        data = ensure_data(list_resp, SuccessTemplateListResponse)
        templates = data.templates
        if templates.__class__.__name__ == "Unset" or not templates:
            self.fail("no templates available")
        source = templates[0]
        source.spec.warm_processes = [
            WarmProcessSpec(
                type_=WarmProcessSpecType.CMD,
                alias="codex",
                command=["sh", "-lc", "touch /tmp/ready; tail -f /dev/null"],
                cwd="/workspace",
            )
        ]

        template_id = f"sdk-py-e2e-{time.time_ns()}"
        created = ensure_data(
            create_template(
                client=client.api,
                body=TemplateCreateRequest(template_id=template_id, spec=source.spec),
            ),
            SuccessTemplateResponse,
        )
        deleted = False

        def _cleanup() -> None:
            if deleted:
                return
            try:
                delete_template(client=client.api, id=template_id)
            except Exception:
                pass

        self.addCleanup(_cleanup)
        self.assertEqual(created.template_id, template_id)
        self.assertEqual(len(created.spec.warm_processes), 1)
        self.assertEqual(created.spec.warm_processes[0].type_, WarmProcessSpecType.CMD)

        fetched = ensure_data(get_template(client=client.api, id=template_id), SuccessTemplateResponse)
        self.assertEqual(fetched.template_id, template_id)
        self.assertEqual(len(fetched.spec.warm_processes), 1)

        updated_spec = fetched.spec
        updated_spec.display_name = "SDK PY E2E Updated"
        update_req = TemplateUpdateRequest(spec=updated_spec)
        updated = ensure_data(update_template(client=client.api, id=template_id, body=update_req), SuccessTemplateResponse)
        self.assertEqual(updated.template_id, template_id)
        self.assertEqual(len(updated.spec.warm_processes), 1)

        ensure_model(delete_template(client=client.api, id=template_id), SuccessMessageResponse)
        deleted = True
