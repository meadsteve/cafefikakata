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

### Requirement Three - Different cafes have different prices
Extend the above so we can have multiple shops with
different prices

### Requirement Four - Stock levels
A cafe has limited stock. When it's sold out orders can't be
placed for that time.

### Requirement Five - Closing down
When a cafe has no stock of any kind it closes down.

### Requirement Six - Let's take fika international
All the previous requirements dealt in Krona. 
Now we want to launch in new countries. Each cafe
should only work in a single currency. 

### Requirement Seven - Special offers
There's now a special offer on the bullar.
If a customer buys 3 they only pay 25kr.

## Considerations
Part of the focus of this Kata is using the type system 
with mypy. 

When defining your functions and classes start to think 
about what types they will receive and output. Dataclasses 
added in 3.7 can also help with this.
