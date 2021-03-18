import twint

# Configure
c = twint.Config()
c.Search = "fruit"

# Run
twint.run.Search(c)
