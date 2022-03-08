
class Helper:

    @staticmethod
    def db_result_to_dict(result):
        try:
            unpacked = [{k: item[k] for k in item.keys()} for item in result]
            return unpacked
        except Exception as e:
            print(f"Failed to execute with error:\n{e}")
            return []