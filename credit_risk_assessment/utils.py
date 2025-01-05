import razorpay

client = razorpay.Client(auth=("your-key", "your-secret"))

payments = client.payment.all({"from": "2021-01-01", "to": "2021-12-31"})
for payment in payments['items']:
    print(payment)
