#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <iterator>
#include <bits/stdc++.h>

using namespace std;

map<char, string> codes;

struct Node
{
    char data;             // One of the input characters
    int freq;             // Frequency of the character
    Node *left, *right; // Left and right child

    Node(char data, int freq)
    {
        left = right = NULL;
        this->data = data;
        this->freq = freq;
    }
};

struct comp
{
    bool operator()(Node* l, Node* r)
    {
        return (l->freq > r->freq);
    }
};

priority_queue<Node*, vector<Node*>, comp> tree;

void storeCodes(struct Node* root, string str)
{
    if (root==NULL)
        return;
    if (root->data != '$')
        codes[root->data]=str;
    storeCodes(root->left, str + "0");
    storeCodes(root->right, str + "1");
}

void huffman (map<char,int> freq,int size)
{
  struct Node *left, *right, *top;
  for (map<char,int>::iterator v=freq.begin(); v!=freq.end(); v++)
      tree.push(new Node(v->first, v->second));
  //std::cout << tree.size() << '\n';
  while (tree.size() != 1)
  {
      left = tree.top();
      tree.pop();
      right = tree.top();
      //std::cout << "lr "<<left->freq<<" "<<right->freq << '\n';
      tree.pop();
      top = new Node('$', left->freq + right->freq);
      top->left = left;
      top->right = right;
      tree.push(top);
  }
  storeCodes(tree.top(), "");
}

string decode(struct Node* root, string s)
{
    string ans = "";
    struct Node* curr = root;
    for (int i=0;i<s.size();i++)
    {
        if (s[i] == '0')
           curr = curr->left;
        else
           curr = curr->right;

        // reached leaf node
        if (curr->left==NULL and curr->right==NULL)
        {
            ans += curr->data;
            curr = root;
        }
    }
    // cout<<ans<<endl;
    return ans+'\0';
}

int main() {
  string s;
  string encodedString, decodedString;
  std::cin >> s;

  map<char, int> map;
  for (int i = 0; i < s.length(); i++) {
    map[s[i]]++;
  }

  std::cout << "Character With there Frequency:" << '\n';
  for(auto it:map)
  {
    std::cout <<it.first<<" "<<it.second<< '\n';
  }

  huffman(map,s.length());

  cout << "Character With there Codes:\n";
  for (auto v=codes.begin(); v!=codes.end(); v++)
      cout << v->first <<' ' << v->second << endl;

  for (auto i: s)
        encodedString+=codes[i];

  cout << "\nEncoded Huffman data:\n" << encodedString << endl;

  decodedString = decode(tree.top(), encodedString);
  cout << "\nDecoded Huffman Data:\n" << decodedString << endl;
  return 0;
}
