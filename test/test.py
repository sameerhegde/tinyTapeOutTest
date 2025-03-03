import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start of Test")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Applying Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1
    dut._log.info("Reset Deasserted")

    # Test Case 1: 3 + 2 = 5 (ui_in = 35 -> 0b00100011)
    dut.ui_in.value = 35  # 35 in decimal (0b00100011 →  ui_in[7:4] = 2, ui_in[3:0] = 3)
    await ClockCycles(dut.clk, 2)  # Wait for 2 clock cycles
    dut._log.info(f"Test Case 1: Expected 5, Got {int(dut.uo_out.value)}")
    assert dut.uo_out.value == 5, f"Test Case 1 Failed: Expected 5, Got {int(dut.uo_out.value)}"

    # Test Case 2: 9 + 11 = 20 (ui_in = 155 -> 0b10011011)
    dut.ui_in.value = 155  # 155 in decimal (0b10011011 → ui_in[7:4] = 9, ui_in[3:0] = 11)
    await ClockCycles(dut.clk, 2)  # Wait for 2 clock cycles
    dut._log.info(f"Test Case 2: Expected 20, Got {int(dut.uo_out.value)}")
    assert dut.uo_out.value == 20, f"Test Case 2 Failed: Expected 20, Got {int(dut.uo_out.value)}"
    
    # Test Case 3: 15 + 15 = 30 (ui_in = 255 -> 0b11111111)
    dut.ui_in.value = 255  # 255 in decimal (0b11111111 → ui_in[7:4] = 15, ui_in[3:0] = 15)
    await ClockCycles(dut.clk, 2)  # Wait for 2 clock cycles
    dut._log.info(f"Test Case 2: Expected 30, Got {int(dut.uo_out.value)}")
    assert dut.uo_out.value == 30, f"Test Case 2 Failed: Expected 30, Got {int(dut.uo_out.value)}"


    dut._log.info("All test cases passed successfully!")

