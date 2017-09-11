on_api =['printTree', 'universes.raw', 'universes.www']
gem_api = ['GetStats']
all_files = on_api + gem_api
settings = dict(onApi=on_api,
                gemApi=gem_api,
                files_to_db_update=all_files,
                instance_type="prod")

