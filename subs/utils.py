from datetime import date, datetime

def AssignBoardTimelineTags(request, board_entry, first_reg):        # abstract some of this into utils so it's less messy
        if (date.today() - first_reg).days <= (board_entry.board.cycle_1_length * 365):
            board_entry.timeline_tag = '1'
            board_entry.save()
        else:
            board_entry.timeline_tag = '2'
            board_entry.save()
