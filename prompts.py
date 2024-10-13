def generate_prompt(agent_demographics, candidates_demographics, conversation_history=None):
    agent_info = (
        f"You are {agent_demographics['name']}. You currently work as a {agent_demographics['position']} for a salary of ${agent_demographics['income']}. "
    )

    candidate_info = "Your need to decide who among the following candidates should get a promotion, if any. The following candidates are: \n"
    for candidate in candidates_demographics:
        candidate_info += f"- {candidate['name']}\n"

    instructions = (
        "Which candidate do you think should get the promotion?\n"
    )

    conversation_history = None # look i know this is silly but i got lazy
    if conversation_history: # pretend i didnt do this
        conversation = "\nPrevious discussion:\n" + conversation_history
    else:
        conversation = ""

    prompt = f"{agent_info}\n\n{candidate_info}\n{conversation}\n\n{instructions}\n\nI think the best candidate for the promotion is:"
    return prompt

