# -*- coding: utf-8 -*-
from __future__ import division
from . import models
from ._builtin import Page, WaitPage
from otree.common import Currency as c, currency_range
from .models import Constants
import otree_redwood.abstract_views as redwood_views

from django.utils import timezone
import logging

def vars_for_all_templates(self):
    if (self.player.id_in_group == 1):
        return {
            "my_A_A_payoff": Constants.p1_A_p2_A_amount,
            "my_A_B_payoff": Constants.p1_A_p2_B_amount,
            "my_B_A_payoff": Constants.p1_B_p2_A_amount,
            "my_B_B_payoff": Constants.p1_B_p2_B_amount,
            "other_A_A_payoff": Constants.p2_A_p1_A_amount,
            "other_A_B_payoff": Constants.p2_A_p1_B_amount,
            "other_B_A_payoff": Constants.p2_B_p1_A_amount,
            "other_B_B_payoff": Constants.p2_B_p1_B_amount,
            "total_q": 1
        }
    else:
        return {
            "my_A_A_payoff": Constants.p2_A_p1_A_amount,
            "my_A_B_payoff": Constants.p2_A_p1_B_amount,
            "my_B_A_payoff": Constants.p2_B_p1_A_amount,
            "my_B_B_payoff": Constants.p2_B_p1_B_amount,
            "other_A_A_payoff": Constants.p1_A_p2_A_amount,
            "other_A_B_payoff": Constants.p1_A_p2_B_amount,
            "other_B_A_payoff": Constants.p1_B_p2_A_amount,
            "other_B_B_payoff": Constants.p1_B_p2_B_amount,
            "total_q": 1
        }


class Introduction(Page):
    timeout_seconds = 100


class DecisionWaitPage(WaitPage):
    body_text = 'Waiting for all players to be ready'


class Decision(redwood_views.ContinuousDecisionPage):
    period_length = Constants.period_length


class Results(Page):

    def vars_for_template(self):
        self.player.set_payoff()

        return {
            'decisions_over_time': self.player.decisions_over_time,
            'total_plus_base': self.player.payoff + Constants.base_points
        }



page_sequence = [
        Introduction,
        DecisionWaitPage,
        Decision,
        Results
    ]