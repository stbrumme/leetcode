class Solution {
public:
    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        if (words.empty())
            return {};

        // creates lines
        vector<vector<string>> text;
        vector<string> line;

        while (!words.empty())
        {
            auto w = words.front();
            words.erase(words.begin());

            if (line.empty())
            {
                line = { w };
            }
            else
            {
                auto used = 0;
                for (auto l : line)
                    used += l.size();
                used += line.size() - 1;

                if (used + 1 + w.size() > maxWidth)
                {
                    text.push_back(line);
                    line = { w };
                }
                else
                {
                    line.push_back(w);
                }
            }
        }

        if (!line.empty())
            text.push_back(line);

        // justify

        vector<string> result;
        for (int i = 0; i < text.size() - 1; i++)
        {
            auto& l = text[i];
            // single word
            if (l.size() == 1)
            {
                auto one = l.front();
                while (one.size() < maxWidth)
                    one += ' ';
                result.push_back(one);
                continue;
            }

            int need = maxWidth;
            for (auto w : l)
                need -= w.size();

            string line = l.front();
            for (int j = 1; j < l.size(); j++)
            {
                int all   = need / (l.size() - 1);
                int extra = need % (l.size() - 1);

                while (all-- > 0)
                    line += ' ';
                if (extra >= j)
                    line += ' ';

                line += l[j];
            }

            result.push_back(line);
        }

        // last line
        string last;
        for (auto l : text.back())
        {
            if (!last.empty())
                last += ' ';
            last += l;
        }
        while (last.size() < maxWidth)
            last += ' ';
        result.push_back(last);

        return result;
    }
};
