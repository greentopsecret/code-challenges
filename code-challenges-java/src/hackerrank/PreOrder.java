package hackerrank;

import java.util.*;
import java.io.*;

class PreOrder {

    static class Node {
        Node left;
        Node right;
        int data;

        Node(int data) {
            this.data = data;
            left = null;
            right = null;
        }

        @Override
        public String toString() {
            return String.format("%d", data);
        }
    }

    public static void preOrder(Node node) {
        if (node == null) {
            return;
        }
        System.out.printf("%s ", node);
        preOrder(node.left);
        preOrder(node.right);
    }

    public static Node insert(Node root, int data) {
        if (root == null) {
            return new Node(data);
        } else {
            Node cur;
            if (data <= root.data) {
                cur = insert(root.left, data);
                root.left = cur;
            } else {
                cur = insert(root.right, data);
                root.right = cur;
            }
            return root;
        }
    }

    public static void main(String[] args) {
        PreOrder.Node root = new PreOrder.Node(1);
        root.right = new PreOrder.Node(2);
        root.right.right = new PreOrder.Node(5);
        root.right.right.left = new PreOrder.Node(3);
        root.right.right.right = new PreOrder.Node(6);
        root.right.right.left.right = new PreOrder.Node(4);

        preOrder(root);

        System.out.println("");

        PreOrder.Node root2 = insert(null, 1);
        insert(root2, 2);
        insert(root2, 5);
        insert(root2, 3);
        insert(root2, 6);
        insert(root2, 4);

        preOrder(root);
    }
}