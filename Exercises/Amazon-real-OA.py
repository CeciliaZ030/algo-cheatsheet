def fetchItemsToDisplay(numItems, items, param, order, perPage, pageNum):
		
		def quicksort_key(keys_list):
			if len(keys_list) == 0 or len(keys_list) == 1:
				return keys_list
			pivot = keys_list[-1]
			l = [k for k in keys_list if k < pivot]
			m = [k for k in keys_list if k == pivot]
			r = [k for k in keys_list if k > pivot]
			return quicksort_key(l) + m + quicksort_key(r)
		
		def quicksort_val(items_list, param):
			if len(items_list) == 0 or len(items_list) == 1:
				return items_list
			pivot = items_list[-1][1][param-1]
			print(items_list, pivot)
			l = [k for k in items_list if k[1][param-1] < pivot]
			m = [k for k in items_list if k[1][param-1] == pivot]
			r = [k for k in items_list if k[1][param-1] > pivot]
			return quicksort_val(l, param) + m + quicksort_val(r, param)

		if param == 0:
			keys_list = [i for i in items.keys()]
			sorted_keys = quicksort_key(keys_list)
			return [sorted_keys[i] for i in range(perPage*pageNum, perPage*(pageNum+1)) if i < numItems]
		else:
			items_list = [i for i in items.items()]
			sorted_items = quicksort_val(items_list, param)
			print(sorted_items)
			return [sorted_items[i][0] for i in range(perPage*pageNum, perPage*(pageNum+1)) if i < numItems]

a = fetchItemsToDisplay(3, {'item1': [10, 15], 'item2': [3, 4], 'item3': [17, 18]}, 0, 1, 2, 1)
print(a)


class Solution(object):
    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        moves = [[1, 2], [2, 1], [-1, 2], [-2, 1], [-1, -2], [-2, -1], [1, -2], [-2, 1]]
        
        def BFS(p, q):
            
            queue = []
            visited = []
            
            queue.append([p, q, 0])
            
            while queue:
                
                min_dist, min_index = -1, -1
                for i in range(len(queue)):
                    dist = abs(queue[i][0] - x) + abs(queue[i][1] - y)
                    if dist < min_dist:
                        min_dist = dist
                        min_index = i
                
                first = queue.pop(i)
                step = first[2] + 1
                visited.append(first)
                print(queue, first)
                
                for move in moves:
                    nextt = [first[0] + move[0], first[1] + move[1]]
                    if nextt == [x, y]:
                        return step
                    if nextt not in visited:
                        queue.append(nextt + [step])
                    else:
                        continue
            
        return BFS(0, 0)
	