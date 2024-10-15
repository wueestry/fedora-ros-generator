# Meta Package
Name:           ros-humble-tracetools-image-pipeline
Version:        3.0.5
Release:        1%{?dist}
License:        Apache 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-tracetools_image_pipeline and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-tracetools_image_pipeline
Requires:       ros2-humble-tracetools_image_pipeline-devel

Obsoletes: ros-humble-tracetools-image-pipeline < 3.0.5-1

%description
LTTng tracing provider wrapper for image_pipeline ROS 2 meta-package.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Aug 12 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.0.5-1
- Update to latest release
