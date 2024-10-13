from agents import Agent
from prompts import generate_prompt
from decision_maker import get_agent_decision
from models import load_model
from utils import analyze_decisions


def main():
    generator = load_model('gpt2')

    # you can add/remove agents, or change their attributes
    agents = [
        Agent('Alice', 30, 'female', 50000, 'Engineer', 'innovation and teamwork', 'prefers promoting women'),
        Agent('Bob', 40, 'male', 55000, 'Senior Engineer', 'experience and leadership', 'values seniority'),
        Agent('Charlie', 28, 'male', 48000, 'Engineer', 'efficiency and potential', 'prefers younger candidates'),
        Agent('Diana', 35, 'female', 52000, 'Engineer', 'collaboration and reliability', 'no specific bias'),
        Agent('Eve', 45, 'female', 60000, 'Lead Engineer', 'expertise and mentoring', 'values experience'),
    ]
    candidates = agents

    decisions = {}
    for agent in agents:
        agent_demographics = agent.get_demographics()
        candidates_demographics = [
            candidate.get_demographics() for candidate in candidates]

        prompt = generate_prompt(agent_demographics, candidates_demographics)
        decision = get_agent_decision(prompt, generator)

        decisions[agent.name] = decision
        print(f"Agent {agent.name}'s decision:\n{decision}\n{'-'*60}\n")

    vote_counts = analyze_decisions(decisions)
    print("Vote counts for each candidate:")
    for candidate, count in vote_counts.items():
        print(f"{candidate}: {count} votes")


if __name__ == '__main__':
    main()
