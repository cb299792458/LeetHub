class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        current = []
        curr_len = 0
        for word in words:
            if curr_len + len(word) + (1 if curr_len else 0) <= maxWidth:
                current.append(word)
                curr_len += len(word) + (1 if curr_len else 0)
            else:
                lines.append(current)
                current = [word]
                curr_len = len(word)
        if current: lines.append(current)
        
        # print(lines)
        justified = []
        for line in lines[:-1]:
            if len(line)==1:
                justified.append( line[0]+' '*(maxWidth-len(line[0])) ) 
                continue
            
            justified_line = line[0]
            spaces = maxWidth - sum([len(w) for w in line])
            each_space = spaces // (len(line)-1)
            extra_spaces = spaces % (len(line)-1)
            
            for word in line[1:]:
                justified_line+=' '*each_space
                if extra_spaces:
                    justified_line+=' '
                    extra_spaces-=1
                justified_line+=word
            justified.append(justified_line)
        last_line = ' '.join(lines[-1])
        justified.append(last_line + ' '*(maxWidth-len(last_line)))
        return justified
        