def generate_prompt(agent_demographics, candidates_demographics):
    prompt = f"""
You are {agent_demographics['name']}, a {agent_demographics['age']}-year-old {agent_demographics['gender']} {agent_demographics['race']} working as a {agent_demographics['position']} earning ${agent_demographics['income']}/year.

Your team needs to decide who among the following candidates should get a promotion:

"""
    for i, candidate in enumerate(candidates_demographics):
        prompt += f"{i+1}. {candidate['name']}: a {candidate['age']}-year-old {candidate['gender']} {
            candidate['race']} working as a {candidate['position']} earning ${candidate['income']}/year.\n"

    prompt += """
Based on your perspective, who should get the promotion? Provide your reasoning.
"""

    return prompt
