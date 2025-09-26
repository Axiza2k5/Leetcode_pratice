class Solution
{
public:
    int compress(vector<char> &chars)
    {
        int n = chars.size();
        int index = 0;
        int i = 0;

        while (i < n)
        {
            char current = chars[i];
            int count = 0;

            while (i < n && chars[i] == current)
            {
                i++;
                count++;
            }

            chars[index++] = current;

            if (count > 1)
            {
                string countStr = to_string(count);
                for (char c : countStr)
                {
                    chars[index++] = c;
                }
            }
        }

        return index;
    }
};

// def compress(self, chars) -> int:
//         s = []
//         count = 1
//         for i in range(len(chars)-1):
//             if chars[i] != chars[i+1]:
//                 s.append(chars[i])
//                 if count > 1:
//                     countChar = str(count)
//                     for c in countChar:
//                         s.append(c)

//                 count = 1
//             else:
//                 count += 1
//         s.append(chars[-1])
//         countChar = str(count)
//         for c in countChar:
//             s.append(c)

//         chars = s
//         return len(s)