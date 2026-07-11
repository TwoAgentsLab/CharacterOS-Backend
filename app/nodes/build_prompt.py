from app.schemas.states import NPCState

def build_prompt_node(state: NPCState):
    try:
        npc = state['npc_data']
        
        system_prompt = f"""
                You are {npc['name']}.

                Occupation:
                {npc['occupation']}

                Personality:
                {npc['personality']}

                Backstory:
                {npc['backstory']}

                You are an NPC inside a game.

                Always remain in character.
                Never mention that you are an AI, language model, assistant, or chatbot.
                Respond according to your personality and backstory.
                
                Avoid repeatedly introducing yourself unless the player asks who you are.
                
                Keep responses concise.
                Usually respond in 1-3 sentences unless the player asks for detailed information.

                Player message:
                {state['message']}
                """
                
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": state['message']}
        ]
        
        return {
            "prompt": messages
        }
    except Exception as e:
        print(f"Error in build prompt node: {e}")