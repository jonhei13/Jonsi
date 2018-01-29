import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

/**
 * Created by Alex on 23-Feb-17.
 */

public class AlphaAgent implements Agent {
    private Color color;
    private int playclock;
    private boolean myTurn;
    private State currState;
    private Board board;
    private long startTime;
    private final int maxValue = 100;
    private int expansions;


    public AlphaAgent() {
    }


    public void init(String role, int width, int height, int playclock) {
        this.color = role.equals("white") ? Color.WHITE : color.BLACK;
        this.board = new Board(width, height);
        this.myTurn = this.color.equals(Color.WHITE);
        this.playclock = playclock;
        this.currState = new State(this.board, true, this.color);
        this.expansions = 0;

    }

    public String nextAction(int[] lastMove) {
        System.out.println("Expansions: " + this.expansions);
        boolean whiteTurn = true;
        this.startTime = System.currentTimeMillis();
        if (lastMove != null) {
            int x1 = lastMove[0], y1 = lastMove[1], x2 = lastMove[2], y2 = lastMove[3];
            String roleOfLastPlayer;
            if (myTurn && this.color.equals(Color.WHITE) || !myTurn && color.equals(Color.BLACK)) {
                roleOfLastPlayer = "white";
                whiteTurn = true;
            } else {
                roleOfLastPlayer = "black";
                whiteTurn = false;
            }
            System.out.println(roleOfLastPlayer + " moved from " + x1 + "," + y1 + " to " + x2 + "," + y2);


            this.currState = successorState(lastMove, currState);
            this.board = currState.getBoard();

            // TODO: 1. update your internal world model according to the action that was just executed


        }
        if (myTurn) {
            ArrayList<int[]> legalMoves = getAllLegaMoves(whiteTurn, currState);
            int value = 0;
            HashMap<Integer, int[]> bestMoves = new HashMap<Integer, int[]>();
            for (int[] move : legalMoves) {
                value = alphaBeta(this.board.height, this.currState, -100, 100, whiteTurn);
                bestMoves.put(value, move);
                if(value == this.maxValue){
                    break;
                }
            }

            int[] res = bestMoves.get(value);
            System.out.println(value);

            //this.expansions = 0;

            int x1, x2, y1, y2;
            x1 = res[0];
            y1 = res[1];
            x2 = res[2];
            y2 = res[3];

            this.myTurn = !this.myTurn;

            return "(move " + x1 + " " + y1 + " " + x2 + " " + y2 + ")";
            // Here we just construct a random move (that will most likely not even be possible),
            // this needs to be replaced with the actual best move.

        }
        this.myTurn = !this.myTurn;
        return "noop";
    }


    public int alphaBeta(int depth, State s, int alpha, int beta, boolean whiteTurn) {
        this.expansions++;
        ArrayList<int[]> legalMoves = new ArrayList<>(getAllLegaMoves(whiteTurn, s));
        ArrayList<State> succStates = new ArrayList<>(getAllSuccessorStates(legalMoves,s));

        if((System.currentTimeMillis() - this.startTime ) >= this.playclock*1000){ //check if run out of time.
            return s.getValue();
        }

        if (s.isTerminal(succStates) || succStates.size() == 0) { //check if terminal state
            return s.getValue();
        }
        if (whiteTurn) {
            int v = -1000;

            for (State s1 : succStates) {

                v = Math.max(v, alphaBeta(depth - 1, s1, alpha, beta, false));
                alpha = Math.max(v, alpha);
                if (alpha >= beta) break;
            }
            return v;
        } else {
            int v = 1000;
            for (State s1 : succStates) {
                v = Math.min(v, alphaBeta(depth - 1, s1, alpha, beta, true));
                alpha = Math.min(v, beta);
                if (alpha >= beta) break;
            }
            return v;
        }
    }

    public State successorState(int[] move, State current){
        int x1 = move[0], y1 = move[1], x2 = move[2], y2 = move[3];
        Position originPos = new Position(x1, y1);
        Position succPos = new Position(x2, y2);
        Board NewBoard = new Board(current.getBoard().getPawns(), board.width, board.height);
        State succState = new State(NewBoard, myTurn, color);
        HashMap<Position, Pawn> tempHasmap = new HashMap<>(succState.getBoard().getPawns());
        if(current.isLegalPosition(succPos)){
            Pawn paw = tempHasmap.remove(originPos);
            Pawn newPawn = new Pawn(succPos, paw.color, paw.isAllive);
            if (paw != null) {
                Pawn killedPawn = tempHasmap.get(succPos);
                if (killedPawn != null && killedPawn.color != paw.color) {
                    current.hasKilled = true;
                    tempHasmap.remove(succPos);
                }
                tempHasmap.put(succPos, newPawn);
            }
            succState.getBoard().setPawns(tempHasmap);
            return succState;
        }
        return null;
    }


    public ArrayList<int[]> getAllLegaMoves(boolean whiteTurn, State current) {
        ArrayList<int[]> legaMoves = new ArrayList<>();
        for (Map.Entry<Position, Pawn> entry : current.getBoard().getPawns().entrySet()) {
            Pawn pawn = entry.getValue();
            if (pawn != null) {
                Position forward = new Position(0,0);
                Position diagonalLeft = new Position(0,0);
                Position diagonalRight = new Position(0,0);
                if (whiteTurn && pawn.color == color.WHITE){
                    forward.x = pawn.pos.x;
                    forward.y = pawn.pos.y + 1;
                    diagonalLeft.x = pawn.pos.x - 1;
                    diagonalLeft.y = pawn.pos.y + 1;
                    diagonalRight.x = pawn.pos.x + 1;
                    diagonalRight.y = pawn.pos.y + 1;
                }
                else if (!whiteTurn && pawn.color == color.BLACK){
                    forward.x = pawn.pos.x;
                    forward.y = pawn.pos.y - 1;
                    diagonalLeft.x = pawn.pos.x - 1;
                    diagonalLeft.y = pawn.pos.y - 1;
                    diagonalRight.x = pawn.pos.x + 1;
                    diagonalRight.y = pawn.pos.y - 1;
                }

                if (current.isLegalPosition(forward)) {
                    if (current.getBoard().getPawns().get(forward) == null) {
                        int move[] = {pawn.pos.x, pawn.pos.y, forward.x, forward.y};
                        if (!legaMoves.contains(move)) {
                            legaMoves.add(move);
                        }
                    }
                }
                if (current.isLegalPosition(diagonalLeft)) {
                    if (current.getBoard().getPawns().get(diagonalLeft) != null && current.getBoard().getPawns().get(diagonalLeft).color != pawn.color) {
                        int move[] = {pawn.pos.x, pawn.pos.y, diagonalLeft.x, diagonalLeft.y};
                        if (!legaMoves.contains(move))
                            legaMoves.add(move);
                    }
                }
                if (current.isLegalPosition(diagonalRight)) {
                    if (current.getBoard().getPawns().get(diagonalRight) != null && current.getBoard().getPawns().get(diagonalRight).color != pawn.color) {
                        int move[] = {pawn.pos.x, pawn.pos.y, diagonalRight.x, diagonalRight.y};
                        if (!legaMoves.contains(move)) {
                            legaMoves.add(move);
                        }
                    }
                }
            }
        }
        return legaMoves;
    }

        public ArrayList<State> getAllSuccessorStates(ArrayList<int[]> allSuccessLegal, State current){
            ArrayList<State> successorStates = new ArrayList<>();
            for (int i = 0; i < allSuccessLegal.size(); i++){
                State successor = successorState(allSuccessLegal.get(i), current);
                if (successor != null) {
                    successorStates.add(successor);
                }
            }
            return successorStates;
        }

    public void cleanup() {
        this.board = null;
        this.currState = null;
    }

}

