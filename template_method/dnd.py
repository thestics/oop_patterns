#!/usr/bin/env python3
# -*-encoding: utf-8-*-
# Author: Danil Kovalenko
import abc


class NPC:
    
    @abc.abstractmethod
    def _pick_up_weapon(self):
        pass
    
    @abc.abstractmethod
    def _defence_action(self):
        pass
    
    @abc.abstractmethod
    def _move_to_safety(self):
        pass
    
    def defend_against_attack(self):
        self._pick_up_weapon()
        self._defence_action()
        self._move_to_safety()


class Pirate(NPC):
    
    def _pick_up_weapon(self):
        print('Pick up sword')
    
    def _defence_action(self):
        print('Defence with sword')
    
    def _move_to_safety(self):
        print('Return to the ship')


class Troll(NPC):
    
    def _pick_up_weapon(self):
        print('Pick up club')
    
    def _defence_action(self):
        print('Defence with club')
    
    def _move_to_safety(self):
        print('Return to the cave')


if __name__ == '__main__':
    Pirate().defend_against_attack()
    Troll().defend_against_attack()
