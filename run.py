from voyager import Voyager

# # You can also use mc_port instead of azure_login, but azure_login is highly recommended
# azure_login = {
#     "client_id": "bda27008-35f0-4ac9-ba57-ba38498ce816",
#     "redirect_url": "https://127.0.0.1/auth-response",
#     "secret_value": "7ls8Q~6oJqjzrxhZn6b11gE4ij78KykE0K72Nbrn",
#     "version": "fabric-loader-0.14.18-1.19", # the version Voyager is tested on
# }
# env_wait_ticks=100
mc_port = 61365
openai_api_key = "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"

voyager = Voyager(
    resume=True,
    mc_port = mc_port,
    # env_wait_ticks=env_wait_ticks,
    openai_api_key=openai_api_key,
)

# start lifelong learning
# voyager.learn(reset_env=False)
voyager.learn()