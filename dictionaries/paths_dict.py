import pathlib

curr_dir = pathlib.Path(__file__).parent.resolve()

root_path = pathlib.Path(f"{curr_dir}/..").resolve()

data_root_path = pathlib.Path(f"{curr_dir}/../data").resolve()

extracted_data_root_path = f"{data_root_path}/extracted_files"

zip_data_root_path = f"{data_root_path}/zip_files"

database_root_path = f"{data_root_path}/enade_data.db"

dictionary_urls = {
    '2017': 'https://download.inep.gov.br/microdados/Enade_Microdados/microdados_Enade_2017_portal_2018.10.09.zip',
    '2018': 'https://download.inep.gov.br/microdados/Enade_Microdados/microdados_enade_2018.zip',
    '2019': 'https://download.inep.gov.br/microdados/Enade_Microdados/microdados_enade_2019.zip'
}

dictionary_extracted_data = {
    "2017": f"{extracted_data_root_path}/2017/3.DADOS/MICRODADOS_ENADE_2017.txt",
    "2018": f"{extracted_data_root_path}/2018/2018/3.DADOS/microdados_enade_2018.txt",
    "2019": f"{extracted_data_root_path}/2019/3.DADOS/microdados_enade_2019.txt",
}

schema_script_path = f"{root_path}/database/database_schema.sql"
