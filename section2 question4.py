class UnderAgeError(Exception):
    pass


class InvalidAgeError(Exception):
    pass


class AgeVerification:

    def set_age(self, age):
        self.age = age

        try:
            if self.age < 0:
                raise ValueError("Age must be a positive number")

            elif self.age < 18:
                raise UnderAgeError("Age must be at least 18")

            elif self.age > 100:
                raise InvalidAgeError("Age must be a reasonable number")

            else:
                print("Age is valid")

        except ValueError as e:
            print(e)

        except UnderAgeError as u:
            print(u)

        except InvalidAgeError as i:
            print(i)

        finally:
            print("Age verification complete")
i=int(input("enter your age:"))
a=AgeVerification()
a.set_age(i)