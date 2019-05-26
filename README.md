# Cafe Fika Kata
## Setup
Locally run `pipenv install`. If you don't have pip installed 
you'll need to run `pip install pipenv` first.

Once this is setup run `./test.sh`

## Kata Requirements
### Requirement One - Pricing
We want to be able to find out the price of some simple items

Coffee - 5kr
Fancy Coffee - 8kr
Kanelbulle - 10kr

### Requirement Two - Basket shopping
We get a list of items from the customer.
What's the total?

### Requirement Three - Special offers
There's now a special offer on the bullar.
If a customer buys 3 they only pay 25kr.

### Requirement Four - Different cafes have different prices
Extend the above so we can have multiple shops with
different prices

### Requirement Four and a half - Different deals
If you only extended the above for prices do
the same for deals

## Considerations
Part of the focus of this Kata is using the type system 
with mypy. 

When defining your functions and classes start to think 
about what types they will receive and output. Dataclasses 
added in 3.7 can also help with this.