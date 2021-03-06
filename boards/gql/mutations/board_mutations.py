import graphene
from graphql_relay import from_global_id

from ...models import Board
from ..types.board_types import BoardType
from graphene_file_upload.scalars import Upload


class BoardInput(graphene.InputObjectType):
    title = graphene.String(required=True)
    content = graphene.String()


class CreateBoardMutation(graphene.Mutation):
    class Arguments:
        input = BoardInput(required=True)
        files = Upload()
    
    board = graphene.Field(BoardType)

    def mutate(self, info, input=None, files=None):
        board = Board()
        for k, v in input.items():
            setattr(board, k, v)
        board.save()
        if files:
            board.photo = files[0]
            board.save()
        return CreateBoardMutation(board=board)


class UpdateBoardMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        input = BoardInput(required=True)
        
    board = graphene.Field(BoardType)

    def mutate(self, info, id, input=None):
        board = Board.objects.get(id=from_global_id(id)[1])
        for k, v in input.items():
            setattr(board, k, v)
        board.save()
        return UpdateBoardMutation(board=board)
