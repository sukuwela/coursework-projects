//// Submitter: minwc (Choi, Min Woo)
//// Partner  : sukuwela (Ukuwela, Shanaya)
//// We certify that we worked cooperatively on this programming
////   assignment, according to the rules for pair programming
//#include <string>
//#include <iostream>
//#include <fstream>
//#include <sstream>
//#include <vector>
//#include <limits>                    //Biggest int: std::numeric_limits<int>::max()
//#include "ics46goody.hpp"
//#include "array_queue.hpp"
//#include "array_priority_queue.hpp"
//#include "array_set.hpp"
//#include "array_map.hpp"
//
//
//typedef ics::ArrayQueue<std::string>              CandidateQueue;
//typedef ics::ArraySet<std::string>                CandidateSet;
//typedef ics::ArrayMap<std::string,int>            CandidateTally;
//
//
//typedef ics::ArrayMap<std::string,CandidateQueue> Preferences;
//typedef ics::pair<std::string,CandidateQueue>     PreferencesEntry;
//
//bool pref_gt(const PreferencesEntry& a,const PreferencesEntry& b){
//    return a.first < b.first;
//}
//
//typedef ics::ArrayPriorityQueue<PreferencesEntry,pref_gt> PreferencesEntryPQ; //Must supply gt at construction
//
//typedef ics::pair<std::string,int>                TallyEntry;
//
//bool a_tally_gt(const TallyEntry& a, const TallyEntry& b){
//    return a.first < b.first;
//}
//
//bool b_tally_gt(const TallyEntry& a, const TallyEntry& b){
//    return a.second < b.second;
//}
//
//typedef ics::ArrayPriorityQueue<TallyEntry>       TallyEntryPQ;
//
//
//
////Read an open file stating voter preferences (each line is (a) a voter
////  followed by (b) all the candidates the voter would vote for, in
////  preference order (from most to least preferred candidate, separated
////  by semicolons), and return a Map of preferences: a Map whose keys are
////  voter names and whose values are a queue of candidate preferences.
//Preferences read_voter_preferences(std::ifstream &file) {
//    CandidateQueue candidates;
//    Preferences voter_map;
//    std::string line;
//    while(getline(file,line)){
//        candidates.enqueue_all(ics::split(line, ";"));
//        voter_map.put(candidates.dequeue(),candidates);
//        candidates.clear();
//    }
//    file.close();
//    return voter_map;
//}
//
//
////Print a label and all the entries in the preferences Map, in alphabetical
////  order according to the voter.
////Use a "->" to separate the voter name from the Queue of candidates.
//void print_voter_preferences(const Preferences& preferences) {
//    std::cout << "Voter name -> queue[Preferences]" << std::endl;
//    PreferencesEntryPQ sorted_pref;
//    sorted_pref.enqueue_all(preferences);
//    for(auto &kv : sorted_pref)
//        std::cout << "  " << kv.first << " -> " << kv.second << std::endl;
//}
//
//
////Print the message followed by all the entries in the CandidateTally, in
////  the order specified by has_higher_priority: i is printed before j, if
////  has_higher_priority(i,j) returns true: sometimes alphabetically by candidate,
////  other times by decreasing votes for the candidate.
////Use a "->" to separate the candidate name from the number of votes they
////  received.
//void print_tally(std::string message, const CandidateTally& tally, bool (*has_higher_priority)(const TallyEntry& i,const TallyEntry& j)) {
//    TallyEntryPQ sorted(has_higher_priority);
//    sorted.enqueue_all(tally);
//    std::cout << message << std::endl;
//    for(auto kv : sorted){
//        std::cout << "  " << kv.first << " -> " << kv.second << std::endl;
//    }
//}
//
//
////Return the CandidateTally: a Map of candidates (as keys) and the number of
////  votes they received, based on the unchanging Preferences (read from the
////  file) and the candidates who are currently still in the election (which changes).
////Every possible candidate should appear as a key in the resulting tally.
////Each voter should tally one vote: for their highest-ranked candidate who is
////  still in the the election.
//CandidateTally evaluate_ballot(const Preferences& preferences, const CandidateSet& candidates) {
//    CandidateTally c_tally;
//    for(auto &kv : preferences){
//        for(auto &v : kv.second){
//            if(candidates.contains(v)) {
//                c_tally[v] += 1;
//                break;
//            }
//        }
//    }
//    return c_tally;
//}
//
//
////Return the Set of candidates who are still in the election, based on the
////  tally of votes: compute the minimum number of votes and return a Set of
////  all candidates receiving more than that minimum; if all candidates
////  receive the same number of votes (that would be the minimum), the empty
////  Set is returned.
//CandidateSet remaining_candidates(const CandidateTally& tally) {
//    CandidateSet remain;
//    TallyEntryPQ sort_it(b_tally_gt);
//    sort_it.enqueue_all(tally);
//    int lowest = sort_it.peek().second;
//    for(auto kv : sort_it){
//        if(kv.second > lowest){
//            remain.insert(kv.first);
//        }
//    }
//    return remain;
//}
//
//
////Prompt the user for a file, create a voter preference Map, and print it.
////Determine the Set of all the candidates in the election, from this Map.
////Repeatedly evaluate the ballot based on the candidates (still) in the
////  election, printing the vote count (tally) two ways: with the candidates
////  (a) shown alphabetically increasing and (b) shown with the vote count
////  decreasing (candidates with equal vote counts are shown alphabetically
////  increasing); from this tally, compute which candidates remain in the
////  election: all candidates receiving more than the minimum number of votes;
////  continue this process until there are less than 2 candidates.
////Print the final result: there may 1 candidate left (the winner) or 0 left
////   (no winner).
//int main() {
//  try {
//      std::ifstream inputfile;
//      ics::safe_open(inputfile, "Enter some voter preferences file name", "votepref1.txt");
//      Preferences vote_pref = read_voter_preferences(inputfile);
//      print_voter_preferences(vote_pref);
//      CandidateSet all;
//      for(auto kv : vote_pref){
//          all.insert_all(kv.second);
//          break;
//          }
//      int count = 0;
//      while(1) {
//          if(all.size() == 1){
//              for(auto c : all) {
//                  std::cout << "  Winner is " << c << std::endl;
//              }
//              break;
//          }
//          if(all.empty()){
//              std::cout << "Not any unique winner: election is a tie among all the candidates remaining on the last ballot" << std::endl;
//              break;
//          }
//          ++count;
//          CandidateTally tally = evaluate_ballot(vote_pref, all);
//          all = remaining_candidates(tally);
//          print_tally("Vote count on ballot #" + std::to_string(count) +
//                      ": candidates (alphabetically ordered) with remaining candidates = " + all.str(), tally,
//                      a_tally_gt);
//          print_tally("Vote count on ballot #" + std::to_string(count) +
//                      ": candidates (numerically ordered) with remaining candidates = " + all.str(), tally, b_tally_gt);
//
//      }
//
//  } catch (ics::IcsError& e) {
//    std::cout << e.what() << std::endl;
//  }
//  return 0;
//}
