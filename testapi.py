import os
import openai
openai.organization = "org-9PXuNSP63FqmNNDhfEMJRr0D"
openai.api_key = os.getenv("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")
openai.Model.list()