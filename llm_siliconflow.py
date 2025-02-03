import llm
from llm.default_plugins.openai_models import Chat

MODELS = {
    "siliconflow/deepseek-reasoner": "deepseek-ai/DeepSeek-R1",
    "siliconflow/deepseek-chat": "deepseek-ai/DeepSeek-V3",
}


class SiliconFlowChat(Chat):
    needs_key = "siliconflow"

    def __init__(self, model_name, model_id):
        super().__init__(
            model_name=model_name,
            model_id=model_id,
            api_base="https://api.siliconflow.cn/v1",
        )

    def __str__(self):
        return "SiliconFlow: {}".format(self.model_id)


@llm.hookimpl
def register_models(register):
    # Only do this if the key is set
    key = llm.get_key("", "siliconflow", "LLM_SILICONFLOW_KEY")
    if not key:
        return

    for model_id, model_name in MODELS.items():
        register(SiliconFlowChat(model_name, model_id))
