"""
LUIT Project Week 12
AWS Service Inventory

Create a list of services using Python. IE: S3, Lambda, EC2, etc

The list should be empty initially.
Populate the list using append or insert.
Print the list and the length of the list.
Remove two specific services from the list by name or by index.
Print the new list and the new length of the list.
"""

# Initalize empty list
aws_services = []

# Populate list using append or insert
aws_services.append('EC2')
aws_services.append('Dynamo DB')
aws_services.append('S3')
aws_services.append('Lamda')
aws_services.append('API Gateway')
aws_services.append('SQS')

# Print the list and the length of the list
print("Printing list of items and length...\n")
print(', '.join(aws_services))
print("Length of list is: " + str(len(aws_services)) + "\n")

# Remove two specific services from the list by name or by index
aws_services.remove('Lamda')
aws_services.pop(2)

# Print the new list and the new lenghth of list
print("Printing new list of items and length...\n")
print(', '.join(aws_services))
print("Length of list is: " + str(len(aws_services)) + "\n")