class Solution {
    public List<String> subdomainVisits(String[] cpdomains) {
        HashMap<String,Integer> map = new HashMap<>();
        ArrayList<String> ans = new ArrayList<>();
        for(String s: cpdomains) {
            String[] med = s.split(" ");
            int num = Integer.valueOf(med[0]);
            String[] dom = med[1].split("\\.");
            String name = "";
            for(int i=dom.length-1;i>=0;i--){
                name = name == "" ?  dom[i]: dom[i]+"."+name;
                if(map.containsKey(name)) map.put(name, map.get(name)+num);
                else map.put(name, num);
            }
        }
            for(String a : map.keySet()){
                ans.add(map.get(a)+" "+a);
            }        
        return ans;
    }
}