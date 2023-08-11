# Import statements


# Main program
if __name__ == "__main__":
    pass

def pickagent() -> str:
    # Choosing the agent
    agent = input("Please choose your agent (Enter 1, 2, 3, or 4)\n", 
          "1. Sage\n",
          "2. Jett\n",
          "3. Sova\n",
          "4. Omen\n"
         )
    agentlist = {1 : "Sage",
                 2 : "Jett",
                 3 : "Sova",
                 4 : "Omen"
                }
    agent = agentlist[agent]
    return agent

def main() -> str:
    """
    main program of the game
    """
    # Welcome message
    print("Welcome to Valorant Realms!")
    agent = pickagent()