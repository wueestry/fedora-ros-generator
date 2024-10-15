# Meta Package
Name:           ros-jazzy-moveit-hybrid-planning
Version:        2.10.0
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            http://moveit.ros.org
Summary:        Meta package for ros2-jazzy-moveit_hybrid_planning and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-moveit_hybrid_planning
Requires:       ros2-jazzy-moveit_hybrid_planning-devel

Obsoletes: ros-jazzy-moveit-hybrid-planning < 2.10.0-1

%description
Hybrid planning components of MoveIt 2

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.10.0-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.9.0-1
- Update to latest release
