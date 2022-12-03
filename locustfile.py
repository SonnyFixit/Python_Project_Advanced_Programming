from locust import HttpUser, task
import random


class LocustTests(HttpUser):
    primeNumbersTest = (312, 1679231, 3, 13, 8921, 97, 86,
                    3567891, 1101, 456789, 23672306230986)

    @task
    def primeEndpoint(self):
         self.client.get(f"/prime/{random.choice(self.primeNumbersTest)}")

  

   