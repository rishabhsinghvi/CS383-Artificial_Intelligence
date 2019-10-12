from math import inf
from agent import Agent
from eval_fns import *

class MinimaxAgent(Agent):
    depth_limit = None
    eval_fn = None
    prune = None

    def __init__(self, eval_fn=open_cells, depth_limit=1, prune=False):
        self.depth_limit = depth_limit
        self.eval_fn = eval_fn
        self.prune = prune

    def select_action(self, game, state):
        """
        TODO: Implement the minimax algorithm
        """
        

        
        if state.min_to_play:
            
            actions = game.get_actions(state)
            b_action = actions[0]
            b_score = inf
            
            for action in actions:
                next_state = game.apply_action(state,action)
                

                score = self.max_p(game, next_state, 1)
                if score < b_score:
                    b_action = action
                    b_score = score
            return b_action
        else:
            actions = game.get_actions(state)
            b_action = actions[0]
            b_score = -inf

            for action in actions:
                next_state = game.apply_action(state,action)

                score = self.min_p(game, next_state, 1)
                if score > b_score:
                    b_action = action
                    b_score = score
            return b_action

    

    def min_p(self, game, state, depth):
        if game.is_terminal(state):
            return game.utility(state)
        
        if self.depth_limit != inf and depth == self.depth_limit:
            return self.eval_fn(game, state)
        
        actions = game.get_actions(state)
        b_action = actions[0]
        b_score = inf
        for action in actions:
            next_state = game.apply_action(state, action)
            score = self.max_p(game, next_state, depth + 1)
            if score < b_score:
                b_action = action
                b_score = score
        return b_score

    
    def max_p(self,game,state, depth):
        if game.is_terminal(state):
            return game.utility(state)
        
        if self.depth_limit != inf and depth == self.depth_limit:
            return self.eval_fn(game, state)
        
        actions = game.get_actions(state)
        b_action = actions[0]
        b_score = -inf
        for action in actions:
            next_state = game.apply_action(state, action)
            score = self.min_p(game, next_state,depth + 1)
            if score > b_score:
                b_action = action
                b_score = score
        return b_score