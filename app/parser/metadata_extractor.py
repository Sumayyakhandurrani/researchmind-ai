import re


class MetadataExtractor:

    def extract_title(self, text):

        lines = text.split("\n")

        lines = [l.strip() for l in lines if l.strip()]

        return lines[1] if len(lines) > 1 else "Unknown"


    def extract_year(self, text):

        match = re.search(r"(19|20)\d{2}", text)

        if match:
            return match.group()

        return "Unknown"


    def extract_sections(self, text):

        headings = [
            "Abstract",
            "Introduction",
            "Related Work",
            "Methodology",
            "Methods",
            "Experiments",
            "Results",
            "Discussion",
            "Conclusion",
            "References"
        ]

        found = []

        for h in headings:

            if h.lower() in text.lower():

                found.append(h)

        return found