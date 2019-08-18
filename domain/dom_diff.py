from bs4 import BeautifulSoup


class DomDiff:
    def __init__(self, app_conf=None):
        super().__init__()
        self.result_text = ""
        self.different_dom_list = []
        if app_conf:
            self.TEXT_MAX = int(app_conf["text_max"])
        else:
            self.TEXT_MAX = 200

    def compare(self, html1, html2):
        s1 = BeautifulSoup(html1, "html.parser")
        s2 = BeautifulSoup(html2, "html.parser")
        self._is_same_dom(s1, s2, "", 0)
        return self.different_dom_list

    def _is_same_dom(self, s1, s2, structure, nest):
        # s1, s2の両方がcontentsを持ってない場合は、s1, s2を比較して結果を返す
        if not hasattr(s1, 'contents') and not hasattr(s2, 'contents'):
            if s1 == s2:
                return True
            else:
                self.different_dom_list.append(structure[:-6])
                print(structure[:-6])
                self._print_until_max("+ " + str(s1))
                self._print_until_max("- " + str(s2))
                self.result_text += structure[:-6] + "\n"
                self.result_text += "+ " + str(s1) + "\n"
                self.result_text += "- " + str(s2) + "\n"
                print("")

                return False
        # s1, s2のどちらかのみがcontentsを持ってない場合は、異なる
        elif not hasattr(s1, 'contents') or not hasattr(s2, 'contents'):
            self.different_dom_list.append(structure[:-6])
            print(structure[:-6])
            self._print_until_max("+ " + str(s1))
            self._print_until_max("- " + str(s2))
            print("")
            self.result_text += structure[:-6] + "\n"
            self.result_text += "+ " + str(s1) + "\n"
            self.result_text += "- " + str(s2) + "\n"

            return False

        if len(s1.contents) == len(s2.contents):
            has_error = True
            for i in range(len(s1.contents)):
                tmp_structure = structure
                if s1.contents[i].name:
                    html_tag = s1.contents[i].name
                    if s1.contents[i].get("id"):
                        html_tag += " id:" + s1.contents[i].get("id")
                    if s1.contents[i].get("class"):
                        html_tag += " class:" + str(s1.contents[i].get("class"))
                    tmp_structure += html_tag
                    print(" " * nest + html_tag)
                if not self._is_same_dom(s1.contents[i], s2.contents[i], tmp_structure + " > ", nest + 1):
                    has_error = False
            return has_error
        else:
            self.different_dom_list.append(structure[:-3])
            print(structure[:-3])
            self._print_until_max("+ " + str(s1.contents))
            self._print_until_max("- " + str(s2.contents))
            print("")
            self.result_text += structure[:-3] + "\n"
            self.result_text += "+ " + str(s1.contents) + "\n"
            self.result_text += "- " + str(s2.contents) + "\n"

            return False

    def _print_until_max(self, text):
        if len(text) < self.TEXT_MAX:
            print(text)
        else:
            print(text[:self.TEXT_MAX] + "...")
