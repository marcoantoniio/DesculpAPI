import api, translate


NoAsAService_API = api.get_api_key("NAAS")
excuse = api.get_excuse(NoAsAService_API)
translated_excuse = translate.translate_text(excuse, target_language="pt")

print(translated_excuse)
