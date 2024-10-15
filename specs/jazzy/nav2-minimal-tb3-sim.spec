# Meta Package
Name:           ros-jazzy-nav2-minimal-tb3-sim
Version:        1.0.1
Release:        1%{?dist}
License:        Apache 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-nav2_minimal_tb3_sim and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-nav2_minimal_tb3_sim
Requires:       ros2-jazzy-nav2_minimal_tb3_sim-devel

Obsoletes: ros-jazzy-nav2-minimal-tb3-sim < 1.0.1-1

%description
Nav2 Minimum TurtleBot3 Simulation

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.0.1-1
- Update to latest release
