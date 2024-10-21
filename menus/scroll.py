from utils.cursor import move_cursor

def render_scroll_bar(total_items, items_per_page, current_option, rows, cols, x, y, box_width):
    if rows >= cols:
        scroll_height = rows * 3
        bar_size = max(2, (items_per_page * scroll_height) // total_items)
        bar_position = (current_option * (scroll_height - bar_size)) // (total_items - 1) if total_items > 1 else 0

        for i in range(scroll_height):
            move_cursor(x + cols * (box_width + 1), y + i)
            print("█" if i >= bar_position and i < bar_position + bar_size else "░")
    else:
        scroll_width = cols * (box_width + 1)
        bar_size = max(2, (items_per_page * scroll_width) // total_items)
        bar_position = (current_option * (scroll_width - bar_size)) // (total_items - 1) if total_items > 1 else 0

        move_cursor(x, y + rows * 3)
        for i in range(scroll_width):
            print("■" if i >= bar_position and i < bar_position + bar_size else "═", end='')
        print()
