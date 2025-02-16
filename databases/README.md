This database is about the following story. 


# The evaluation of our system

### Level 1: extract the available knowledge
- client A asks about a number in its database
- client A asks about an information available on the web
- client A asks about a report on its past sales 

### Level 2: mix the information
- analysis should i buy this house in rural france for 40000? 
    expected answer: this client doesn't like living in a city that have few inhabitants. Should invest in a city with more people. 

# The different subdatabases
## The types of query we will have
```
{
    user_: id, 
    question: str, 
}
```
Examples of query? 
- What experience do you have in my industry?
    expected answer: Here are the public project that I made. Public clients. I made they win n$. + more general: 
- Immobilier: should I buy this building? 
    expected answer: here is information about the market. + consideration about plausible stuff (say without explaining what they know)
- can I create this product? 
    expected answer: check the legislation 


{
    query_type: name, 
    methodology_to_solve_the_query: str, 
}

## The clients
{
    firm_id: , 
    firm: , 
    domain_of_activity: , 
}

The databases they shared with you: 
{
    firm_id: , 
    privacy: secret/semiprivate/public, 
    database_description: , 
    who_has_access: , 
}

## The databases
{

}