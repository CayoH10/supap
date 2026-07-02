program exemplo;

var
    x, y : integer;

procedure teste;
begin
    x := 10;
end;

begin
    x := 1;
    y := 2;

    if x < y then
        teste();

    while x < 5 do
    begin
        x := x + 1;
    end;
end.