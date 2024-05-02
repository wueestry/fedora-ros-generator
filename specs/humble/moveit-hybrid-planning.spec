# Meta Package
Name:           ros-humble-moveit-hybrid-planning
Version:        2.5.5
Release:        1%{?dist}
License:        BSD
URL:            http://moveit.ros.org
Summary:        Meta package for ros2-humble-moveit_hybrid_planning and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-moveit_hybrid_planning
Requires:       ros2-humble-moveit_hybrid_planning-devel

Obsoletes: ros-humble-moveit-hybrid-planning < 2.5.5-1

%description
Hybrid planning components of MoveIt 2

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Mar 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.5.5-1
- update to latest release
