class Solution {    
    class CourseComparatorArray implements Comparator<int[]>{
        @Override
        public int compare(int[] c1, int[] c2){
            if(c1[1] < c2[1]){
                return -1;
            } else if(c1[1] > c2[1]){
                return 1;
            } else {
                return 0;
            }
        }
    }
    
    class CourseLengthComparator implements Comparator<int[]>{
        @Override
        public int compare(int[] c1, int[] c2){
            if(c1[0] > c2[0]){
                return -1;
            } else if(c1[0] < c2[0]){
                return 1;
            } else {
                return 0;
            }
        }
    }
    
    String courseToString(int[] course){
        return "length: " + course[0] + "deadline: " + course[1];
    }
    
    public int scheduleCourse(int[][] courses) {
        PriorityQueue<int[]> courseQueue = new PriorityQueue<>(courses.length, new CourseLengthComparator());
        Arrays.sort(courses, new CourseComparatorArray());
        
        int currentDay = 0;
        
        for(int i = 0; i < courses.length; i++){
            if(courses[i][0] + currentDay <= courses[i][1]){
                currentDay += courses[i][0];
                courseQueue.add(courses[i]);
            } else if(courseQueue.size() != 0 && courses[i][0] < courseQueue.peek()[0]){
                currentDay += courses[i][0] - courseQueue.poll()[0];
                courseQueue.add(courses[i]);
            }
        }
        
        
        
        return courseQueue.size();
    }
}
