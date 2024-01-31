import heapq


def get_connection_order(cables):
    heapq.heapify(cables)

    order = []

    while len(cables) > 1:
        cable1 = heapq.heappop(cables)
        cable2 = heapq.heappop(cables)
        cost = cable1 + cable2
        order.append((cable1, cable2))
        heapq.heappush(cables, cost)

    return order


def get_total_cost(orders):
    total_cost = 0

    for order in orders:
        total_cost += order[0] + order[1]

    return total_cost


def main():
    cables = [4, 12, 6, 8]

    connection_order = get_connection_order(cables)
    total_cost = get_total_cost(connection_order)

    print("Порядок з'єднаннь:", connection_order)
    print("Сумарна вартість:", total_cost)


if __name__ == "__main__":
    main()
