# Meta Package
Name:           ros-jazzy-gz-sim-vendor
Version:        0.0.5
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://github.com/gazebosim/gz-sim
Summary:        Meta package for ros2-jazzy-gz_sim_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-gz_sim_vendor
Requires:       ros2-jazzy-gz_sim_vendor-devel

Obsoletes: ros-jazzy-gz-sim-vendor < 0.0.5-1

%description
Vendor package for: gz-sim8 8.6.0 Gazebo Sim : A Robotic Simulator

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Aug 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.0.5-1
- Update to latest release
* Wed Jul 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.0.4-1
- Update to latest release
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.0.3-1
- Update to latest release
