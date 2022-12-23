from locust import HttpUser, task
import random


class LocustTests(HttpUser):
    
    rand = random.randint(1, 63672306230986 )

    primeNumbersTest = (312, 1679231, 3, 13, 8921, 97, 86,
                    3567891, 1101, 456789, 23672306230986, rand )
                    

    @task
    def primeEndpoint(self):
         self.client.get(f"/prime/{random.choice(self.primeNumbersTest)}")

    @task
    def invertImageEndpoint(self):
        rand = random.randint(1, 5)
        with open(f"../testImages/test{rand}.jpg", "rb") as imageFile:
            self.client.post(
                "/picture/invert/", files={"file": ("filename", imageFile, "image/jpeg")})

   