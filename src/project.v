/*
 * Copyright (c) 2024 Sameer Hegde
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

module tt_um_sameerhegde_adder (
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    input  wire [7:0] uio_in,   // IOs: Input path
    output wire [7:0] uio_out,  // IOs: Output path
    output wire [7:0] uio_oe,   // IOs: Enable path (active high: 0=input, 1=output)
    input  wire       ena,      // always 1 when the design is powered, so you can ignore it
    input  wire       clk,      // clock
    input  wire       rst_n     // reset_n - low to reset
);
	reg [4:0] sumTemp;
	always@(posedge clk)begin
		if(!rst_n)begin
			sumTemp <= 'b0;
		end
		else begin
			sumTemp <= ui_in[3:0] + ui_in[7:4]; // [3:0]ui_in input1 & [7:4] ui_in input2 ;
		end
	end

  // All output pins must be assigned. If not used, assign to 0.
  assign uo_out  = {3'b000,sumTemp};
  assign uio_out = 0;
  assign uio_oe  = 0;

  // List all unused inputs to prevent warnings
  wire _unused = &{ena,1'b0};

endmodule
