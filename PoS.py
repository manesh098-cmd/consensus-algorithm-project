 def def pos(self):
     """
        #get other's stakes
        #add owns claim
        #pick winner
        """

        print(str(self.myAccount) + ' =======================> Getting Valid chain\n')
        self.resolve_conflict()
        time.sleep(1)
        self._pos()
        print('***Calling other nodes to announce theirs***' + "\n")
        time.sleep(1)
        for node in self.nodes:
            node._pos()
        time.sleep(1)
        for block in self.tempBlocks:
            validator = block['Validator'].rsplit(', ')
            if validator[0] == self.pick_winner()[0]:
                new_block = block
                break
            else:
                pass
        print('New Block ====> ' + str(new_block) + "\n")
        time.sleep(1)
        self.add_new_block(new_block)
        for node in self.nodes:
            node.add_new_block(new_block)
        print('Process ends' + "\n")
     

 def def _pos(self):
        print("Coming from ==========================> " + str(self.myAccount) + "\n")
        time.sleep(1)
        print('***Generating new stake block***' + "\n")
        time.sleep(1)
        self.generate_new_block()
        print('***Exchanging temporary blocks with other nodes***' + "\n")
        time.sleep(1)
        self.get_blocks_from_nodes()
        print('***Picking a winner***' + "\n")
        time.sleep(1)
        print("Winner is =======================> " + str(self.pick_winner()) + "\n")
