class Validator():
    def login_validation(login: str):
        if len(login) < 6:
            return "ValidationLoginError"
        return True
        
    def password_validation(passsword: str):
        if len(passsword) < 8:
            return "ValidationPasswordError"
        if (passsword == passsword.lower()) or (passsword == passsword.upper()):
            return "ValidationPasswordError"
        if not("!" in passsword or "@" in passsword or "#" in passsword or "$" in passsword or "%" in passsword or ">" in passsword):
            if not("&" in passsword or "*" in passsword or "(" in passsword or ")" in passsword or "-" in passsword):
                if not("_" in passsword or "=" in passsword or "+" in passsword or "?" in passsword or "<" in passsword):
                    return "ValidationPasswordError"
        return True
        
    def email_validation(email: str):
        if not "@" in email:
            return "ValidationEmailError"
        if not "." in email:
            return "ValidationEmailError"
        if not((len(email) == email.find(".") + 3) or (len(email) == email.find(".") + 4)):
            return "ValidationEmailError"
        return True
        
    def validate(self, login: str, password: str, email: str):
        if Validator.login_validation(login) != 1:
            return "ValidationLoginError"
        elif Validator.password_validation(password) != 1:
            return "ValidationPasswordError"
        elif Validator.email_validation(email) != 1:
            return "ValidationEmailError"
        return True
        

def main():
    validator = Validator()
    print(validator.validate("user_login", "Some!Password", "mail@mail.com"))
    print(validator.validate("admin123", "SomeStrange?", "gmail@gmail.ru"))
    print("------------")
    print(validator.validate("user", "Some!Password", "mail@mail.com"))
    print("------------")
    print(validator.validate("user_login", "Pass!", "mail@mail.com"))
    print(validator.validate("user_login", "some!password", "mail@mail.com"))
    print(validator.validate("user_login", "SomePassword", "mail@mail.com"))
    print("------------")
    print(validator.validate("user_login", "Some!Password", "mailmail.com"))
    print(validator.validate("user_login", "Some!Password", "mail@mailcom"))

main()
