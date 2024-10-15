# Meta Package
Name:           ros-jazzy-nav2-smac-planner
Version:        1.3.2
Release:        1%{?dist}
License:        Apache-2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-nav2_smac_planner and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-nav2_smac_planner
Requires:       ros2-jazzy-nav2_smac_planner-devel

Obsoletes: ros-jazzy-nav2-smac-planner < 1.3.2-1

%description
Smac global planning plugin: A*, Hybrid-A*, State Lattice

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Aug 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.3.2-1
- Update to latest release
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.3.1-1
- Update to latest release
