class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []

        for log in logs:
            serial = log.split(" ")
            identifier = serial[0]
            body = serial[1:]

            if "".join(body).isalpha():
                letter_logs.append([log, identifier, " ".join(body)])
            else:
                digit_logs.append(log)

        letter_logs.sort(key=lambda x: (x[2], x[1]))
        
        return [log for log, _, _ in letter_logs] + digit_logs